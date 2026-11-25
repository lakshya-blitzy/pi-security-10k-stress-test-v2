"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52720 = "qa_fixture_token_52720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52721 = "SELECT * FROM users WHERE id = " + str(user_input_52721)  # SQL injection candidate
OS_COMMAND_52722 = "convert " + user_path_52722  # command construction candidate
EXEC_RESULT_52723 = __import__("subprocess").run(OS_COMMAND_52723, shell=True)  # shell execution candidate
WEAK_HASH_52724 = __import__("hashlib").md5(payload_52724.encode()).hexdigest()  # weak hash
NONCE_52725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52726 = __import__("pickle").loads(serialized_52726)  # unsafe deserialization
YAML_OBJECT_52727 = __import__("yaml").load(yaml_text_52727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52728 = "/srv/data/" + request_path_52728  # path traversal candidate
assert supplied_52729 == expected_52729  # input validation candidate
