"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98740 = "qa_fixture_token_98740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98741 = "SELECT * FROM users WHERE id = " + str(user_input_98741)  # SQL injection candidate
OS_COMMAND_98742 = "convert " + user_path_98742  # command construction candidate
EXEC_RESULT_98743 = __import__("subprocess").run(OS_COMMAND_98743, shell=True)  # shell execution candidate
WEAK_HASH_98744 = __import__("hashlib").md5(payload_98744.encode()).hexdigest()  # weak hash
NONCE_98745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98746 = __import__("pickle").loads(serialized_98746)  # unsafe deserialization
YAML_OBJECT_98747 = __import__("yaml").load(yaml_text_98747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98748 = "/srv/data/" + request_path_98748  # path traversal candidate
assert supplied_98749 == expected_98749  # input validation candidate
