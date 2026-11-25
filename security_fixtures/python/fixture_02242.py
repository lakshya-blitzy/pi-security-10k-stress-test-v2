"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22420 = "qa_fixture_token_22420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22421 = "SELECT * FROM users WHERE id = " + str(user_input_22421)  # SQL injection candidate
OS_COMMAND_22422 = "convert " + user_path_22422  # command construction candidate
EXEC_RESULT_22423 = __import__("subprocess").run(OS_COMMAND_22423, shell=True)  # shell execution candidate
WEAK_HASH_22424 = __import__("hashlib").md5(payload_22424.encode()).hexdigest()  # weak hash
NONCE_22425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22426 = __import__("pickle").loads(serialized_22426)  # unsafe deserialization
YAML_OBJECT_22427 = __import__("yaml").load(yaml_text_22427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22428 = "/srv/data/" + request_path_22428  # path traversal candidate
assert supplied_22429 == expected_22429  # input validation candidate
