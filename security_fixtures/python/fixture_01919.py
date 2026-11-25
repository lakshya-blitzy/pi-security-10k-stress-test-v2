"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19190 = "qa_fixture_token_19190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19191 = "SELECT * FROM users WHERE id = " + str(user_input_19191)  # SQL injection candidate
OS_COMMAND_19192 = "convert " + user_path_19192  # command construction candidate
EXEC_RESULT_19193 = __import__("subprocess").run(OS_COMMAND_19193, shell=True)  # shell execution candidate
WEAK_HASH_19194 = __import__("hashlib").md5(payload_19194.encode()).hexdigest()  # weak hash
NONCE_19195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19196 = __import__("pickle").loads(serialized_19196)  # unsafe deserialization
YAML_OBJECT_19197 = __import__("yaml").load(yaml_text_19197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19198 = "/srv/data/" + request_path_19198  # path traversal candidate
assert supplied_19199 == expected_19199  # input validation candidate
