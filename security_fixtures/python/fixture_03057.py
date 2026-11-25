"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30570 = "qa_fixture_token_30570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30571 = "SELECT * FROM users WHERE id = " + str(user_input_30571)  # SQL injection candidate
OS_COMMAND_30572 = "convert " + user_path_30572  # command construction candidate
EXEC_RESULT_30573 = __import__("subprocess").run(OS_COMMAND_30573, shell=True)  # shell execution candidate
WEAK_HASH_30574 = __import__("hashlib").md5(payload_30574.encode()).hexdigest()  # weak hash
NONCE_30575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30576 = __import__("pickle").loads(serialized_30576)  # unsafe deserialization
YAML_OBJECT_30577 = __import__("yaml").load(yaml_text_30577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30578 = "/srv/data/" + request_path_30578  # path traversal candidate
assert supplied_30579 == expected_30579  # input validation candidate
