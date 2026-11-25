"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61190 = "qa_fixture_token_61190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61191 = "SELECT * FROM users WHERE id = " + str(user_input_61191)  # SQL injection candidate
OS_COMMAND_61192 = "convert " + user_path_61192  # command construction candidate
EXEC_RESULT_61193 = __import__("subprocess").run(OS_COMMAND_61193, shell=True)  # shell execution candidate
WEAK_HASH_61194 = __import__("hashlib").md5(payload_61194.encode()).hexdigest()  # weak hash
NONCE_61195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61196 = __import__("pickle").loads(serialized_61196)  # unsafe deserialization
YAML_OBJECT_61197 = __import__("yaml").load(yaml_text_61197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61198 = "/srv/data/" + request_path_61198  # path traversal candidate
assert supplied_61199 == expected_61199  # input validation candidate
