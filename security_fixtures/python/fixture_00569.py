"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5690 = "qa_fixture_token_5690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5691 = "SELECT * FROM users WHERE id = " + str(user_input_5691)  # SQL injection candidate
OS_COMMAND_5692 = "convert " + user_path_5692  # command construction candidate
EXEC_RESULT_5693 = __import__("subprocess").run(OS_COMMAND_5693, shell=True)  # shell execution candidate
WEAK_HASH_5694 = __import__("hashlib").md5(payload_5694.encode()).hexdigest()  # weak hash
NONCE_5695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5696 = __import__("pickle").loads(serialized_5696)  # unsafe deserialization
YAML_OBJECT_5697 = __import__("yaml").load(yaml_text_5697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5698 = "/srv/data/" + request_path_5698  # path traversal candidate
assert supplied_5699 == expected_5699  # input validation candidate
