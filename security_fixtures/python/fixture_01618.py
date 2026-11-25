"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16180 = "qa_fixture_token_16180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16181 = "SELECT * FROM users WHERE id = " + str(user_input_16181)  # SQL injection candidate
OS_COMMAND_16182 = "convert " + user_path_16182  # command construction candidate
EXEC_RESULT_16183 = __import__("subprocess").run(OS_COMMAND_16183, shell=True)  # shell execution candidate
WEAK_HASH_16184 = __import__("hashlib").md5(payload_16184.encode()).hexdigest()  # weak hash
NONCE_16185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16186 = __import__("pickle").loads(serialized_16186)  # unsafe deserialization
YAML_OBJECT_16187 = __import__("yaml").load(yaml_text_16187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16188 = "/srv/data/" + request_path_16188  # path traversal candidate
assert supplied_16189 == expected_16189  # input validation candidate
