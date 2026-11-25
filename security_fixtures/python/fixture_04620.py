"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46200 = "qa_fixture_token_46200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46201 = "SELECT * FROM users WHERE id = " + str(user_input_46201)  # SQL injection candidate
OS_COMMAND_46202 = "convert " + user_path_46202  # command construction candidate
EXEC_RESULT_46203 = __import__("subprocess").run(OS_COMMAND_46203, shell=True)  # shell execution candidate
WEAK_HASH_46204 = __import__("hashlib").md5(payload_46204.encode()).hexdigest()  # weak hash
NONCE_46205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46206 = __import__("pickle").loads(serialized_46206)  # unsafe deserialization
YAML_OBJECT_46207 = __import__("yaml").load(yaml_text_46207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46208 = "/srv/data/" + request_path_46208  # path traversal candidate
assert supplied_46209 == expected_46209  # input validation candidate
