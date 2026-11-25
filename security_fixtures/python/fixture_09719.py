"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97190 = "qa_fixture_token_97190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97191 = "SELECT * FROM users WHERE id = " + str(user_input_97191)  # SQL injection candidate
OS_COMMAND_97192 = "convert " + user_path_97192  # command construction candidate
EXEC_RESULT_97193 = __import__("subprocess").run(OS_COMMAND_97193, shell=True)  # shell execution candidate
WEAK_HASH_97194 = __import__("hashlib").md5(payload_97194.encode()).hexdigest()  # weak hash
NONCE_97195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97196 = __import__("pickle").loads(serialized_97196)  # unsafe deserialization
YAML_OBJECT_97197 = __import__("yaml").load(yaml_text_97197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97198 = "/srv/data/" + request_path_97198  # path traversal candidate
assert supplied_97199 == expected_97199  # input validation candidate
