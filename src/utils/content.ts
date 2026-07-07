import fs from 'node:fs';
import path from 'node:path';
import { parse } from 'yaml';

const CONTENT_DIR = path.resolve(process.cwd(), 'src/content');

export function readYamlFile<T>(fileName: string): T {
  const filePath = path.join(CONTENT_DIR, fileName);
  const fileContent = fs.readFileSync(filePath, 'utf8');
  return parse(fileContent) as T;
}

export interface Profile {
  name: string;
  title: string;
  headline: string;
  summary: string;
  location: string;
  socials: {
    cv: string;
    scholar: string;
    linkedin: string;
    email: string;
    github?: string;
  };
  focus_areas: {
    title: string;
    description: string;
  }[];
}

export interface Project {
  title: string;
  category: string;
  status: string;
  featured: boolean;
  tags: string[];
  problem: string;
  data: string;
  methods: string;
  output: string;
  industry_relevance: string;
}

export interface PublicationItem {
  title: string;
  authors: string;
  venue: string;
  year: number;
  tags: string[];
  summary: string;
  industry_relevance: string;
  link?: string;
}

export interface PublicationGroup {
  group: string;
  items: PublicationItem[];
}

export interface SkillItem {
  name: string;
  description: string;
}

export interface SkillGroup {
  group: string;
  items: SkillItem[];
}

export interface ExperienceRole {
  role: string;
  institution: string;
  period: string;
  advisor?: string;
  bullets: string[];
}

export interface EducationItem {
  degree: string;
  institution: string;
}

export interface ExperienceData {
  roles: ExperienceRole[];
  education: EducationItem[];
}

export function getProfile(): Profile {
  return readYamlFile<Profile>('profile.yaml');
}

export function getProjects(): Project[] {
  return readYamlFile<Project[]>('projects.yaml');
}

export function getPublications(): PublicationGroup[] {
  return readYamlFile<PublicationGroup[]>('publications.yaml');
}

export function getSkills(): SkillGroup[] {
  return readYamlFile<SkillGroup[]>('skills.yaml');
}

export function getExperience(): ExperienceData {
  return readYamlFile<ExperienceData>('experience.yaml');
}
