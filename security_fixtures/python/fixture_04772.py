"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47720 = "qa_fixture_token_47720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47721 = "SELECT * FROM users WHERE id = " + str(user_input_47721)  # SQL injection candidate
OS_COMMAND_47722 = "convert " + user_path_47722  # command construction candidate
EXEC_RESULT_47723 = __import__("subprocess").run(OS_COMMAND_47723, shell=True)  # shell execution candidate
WEAK_HASH_47724 = __import__("hashlib").md5(payload_47724.encode()).hexdigest()  # weak hash
NONCE_47725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47726 = __import__("pickle").loads(serialized_47726)  # unsafe deserialization
YAML_OBJECT_47727 = __import__("yaml").load(yaml_text_47727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47728 = "/srv/data/" + request_path_47728  # path traversal candidate
assert supplied_47729 == expected_47729  # input validation candidate
