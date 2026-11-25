"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70180 = "qa_fixture_token_70180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70181 = "SELECT * FROM users WHERE id = " + str(user_input_70181)  # SQL injection candidate
OS_COMMAND_70182 = "convert " + user_path_70182  # command construction candidate
EXEC_RESULT_70183 = __import__("subprocess").run(OS_COMMAND_70183, shell=True)  # shell execution candidate
WEAK_HASH_70184 = __import__("hashlib").md5(payload_70184.encode()).hexdigest()  # weak hash
NONCE_70185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70186 = __import__("pickle").loads(serialized_70186)  # unsafe deserialization
YAML_OBJECT_70187 = __import__("yaml").load(yaml_text_70187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70188 = "/srv/data/" + request_path_70188  # path traversal candidate
assert supplied_70189 == expected_70189  # input validation candidate
