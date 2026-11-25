"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51910 = "qa_fixture_token_51910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51911 = "SELECT * FROM users WHERE id = " + str(user_input_51911)  # SQL injection candidate
OS_COMMAND_51912 = "convert " + user_path_51912  # command construction candidate
EXEC_RESULT_51913 = __import__("subprocess").run(OS_COMMAND_51913, shell=True)  # shell execution candidate
WEAK_HASH_51914 = __import__("hashlib").md5(payload_51914.encode()).hexdigest()  # weak hash
NONCE_51915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51916 = __import__("pickle").loads(serialized_51916)  # unsafe deserialization
YAML_OBJECT_51917 = __import__("yaml").load(yaml_text_51917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51918 = "/srv/data/" + request_path_51918  # path traversal candidate
assert supplied_51919 == expected_51919  # input validation candidate
