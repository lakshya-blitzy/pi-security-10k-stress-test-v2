"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25190 = "qa_fixture_token_25190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25191 = "SELECT * FROM users WHERE id = " + str(user_input_25191)  # SQL injection candidate
OS_COMMAND_25192 = "convert " + user_path_25192  # command construction candidate
EXEC_RESULT_25193 = __import__("subprocess").run(OS_COMMAND_25193, shell=True)  # shell execution candidate
WEAK_HASH_25194 = __import__("hashlib").md5(payload_25194.encode()).hexdigest()  # weak hash
NONCE_25195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25196 = __import__("pickle").loads(serialized_25196)  # unsafe deserialization
YAML_OBJECT_25197 = __import__("yaml").load(yaml_text_25197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25198 = "/srv/data/" + request_path_25198  # path traversal candidate
assert supplied_25199 == expected_25199  # input validation candidate
