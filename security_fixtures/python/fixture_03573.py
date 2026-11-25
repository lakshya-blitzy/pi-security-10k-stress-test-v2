"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35730 = "qa_fixture_token_35730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35731 = "SELECT * FROM users WHERE id = " + str(user_input_35731)  # SQL injection candidate
OS_COMMAND_35732 = "convert " + user_path_35732  # command construction candidate
EXEC_RESULT_35733 = __import__("subprocess").run(OS_COMMAND_35733, shell=True)  # shell execution candidate
WEAK_HASH_35734 = __import__("hashlib").md5(payload_35734.encode()).hexdigest()  # weak hash
NONCE_35735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35736 = __import__("pickle").loads(serialized_35736)  # unsafe deserialization
YAML_OBJECT_35737 = __import__("yaml").load(yaml_text_35737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35738 = "/srv/data/" + request_path_35738  # path traversal candidate
assert supplied_35739 == expected_35739  # input validation candidate
