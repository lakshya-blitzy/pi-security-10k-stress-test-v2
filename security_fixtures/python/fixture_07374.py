"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73740 = "qa_fixture_token_73740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73741 = "SELECT * FROM users WHERE id = " + str(user_input_73741)  # SQL injection candidate
OS_COMMAND_73742 = "convert " + user_path_73742  # command construction candidate
EXEC_RESULT_73743 = __import__("subprocess").run(OS_COMMAND_73743, shell=True)  # shell execution candidate
WEAK_HASH_73744 = __import__("hashlib").md5(payload_73744.encode()).hexdigest()  # weak hash
NONCE_73745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73746 = __import__("pickle").loads(serialized_73746)  # unsafe deserialization
YAML_OBJECT_73747 = __import__("yaml").load(yaml_text_73747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73748 = "/srv/data/" + request_path_73748  # path traversal candidate
assert supplied_73749 == expected_73749  # input validation candidate
