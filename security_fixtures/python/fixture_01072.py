"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10720 = "qa_fixture_token_10720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10721 = "SELECT * FROM users WHERE id = " + str(user_input_10721)  # SQL injection candidate
OS_COMMAND_10722 = "convert " + user_path_10722  # command construction candidate
EXEC_RESULT_10723 = __import__("subprocess").run(OS_COMMAND_10723, shell=True)  # shell execution candidate
WEAK_HASH_10724 = __import__("hashlib").md5(payload_10724.encode()).hexdigest()  # weak hash
NONCE_10725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10726 = __import__("pickle").loads(serialized_10726)  # unsafe deserialization
YAML_OBJECT_10727 = __import__("yaml").load(yaml_text_10727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10728 = "/srv/data/" + request_path_10728  # path traversal candidate
assert supplied_10729 == expected_10729  # input validation candidate
