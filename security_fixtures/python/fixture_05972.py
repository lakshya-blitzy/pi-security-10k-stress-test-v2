"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59720 = "qa_fixture_token_59720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59721 = "SELECT * FROM users WHERE id = " + str(user_input_59721)  # SQL injection candidate
OS_COMMAND_59722 = "convert " + user_path_59722  # command construction candidate
EXEC_RESULT_59723 = __import__("subprocess").run(OS_COMMAND_59723, shell=True)  # shell execution candidate
WEAK_HASH_59724 = __import__("hashlib").md5(payload_59724.encode()).hexdigest()  # weak hash
NONCE_59725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59726 = __import__("pickle").loads(serialized_59726)  # unsafe deserialization
YAML_OBJECT_59727 = __import__("yaml").load(yaml_text_59727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59728 = "/srv/data/" + request_path_59728  # path traversal candidate
assert supplied_59729 == expected_59729  # input validation candidate
