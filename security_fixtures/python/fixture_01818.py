"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18180 = "qa_fixture_token_18180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18181 = "SELECT * FROM users WHERE id = " + str(user_input_18181)  # SQL injection candidate
OS_COMMAND_18182 = "convert " + user_path_18182  # command construction candidate
EXEC_RESULT_18183 = __import__("subprocess").run(OS_COMMAND_18183, shell=True)  # shell execution candidate
WEAK_HASH_18184 = __import__("hashlib").md5(payload_18184.encode()).hexdigest()  # weak hash
NONCE_18185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18186 = __import__("pickle").loads(serialized_18186)  # unsafe deserialization
YAML_OBJECT_18187 = __import__("yaml").load(yaml_text_18187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18188 = "/srv/data/" + request_path_18188  # path traversal candidate
assert supplied_18189 == expected_18189  # input validation candidate
