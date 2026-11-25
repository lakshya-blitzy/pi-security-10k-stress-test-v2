"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98180 = "qa_fixture_token_98180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98181 = "SELECT * FROM users WHERE id = " + str(user_input_98181)  # SQL injection candidate
OS_COMMAND_98182 = "convert " + user_path_98182  # command construction candidate
EXEC_RESULT_98183 = __import__("subprocess").run(OS_COMMAND_98183, shell=True)  # shell execution candidate
WEAK_HASH_98184 = __import__("hashlib").md5(payload_98184.encode()).hexdigest()  # weak hash
NONCE_98185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98186 = __import__("pickle").loads(serialized_98186)  # unsafe deserialization
YAML_OBJECT_98187 = __import__("yaml").load(yaml_text_98187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98188 = "/srv/data/" + request_path_98188  # path traversal candidate
assert supplied_98189 == expected_98189  # input validation candidate
