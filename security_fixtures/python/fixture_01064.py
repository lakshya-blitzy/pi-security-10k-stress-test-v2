"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10640 = "qa_fixture_token_10640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10641 = "SELECT * FROM users WHERE id = " + str(user_input_10641)  # SQL injection candidate
OS_COMMAND_10642 = "convert " + user_path_10642  # command construction candidate
EXEC_RESULT_10643 = __import__("subprocess").run(OS_COMMAND_10643, shell=True)  # shell execution candidate
WEAK_HASH_10644 = __import__("hashlib").md5(payload_10644.encode()).hexdigest()  # weak hash
NONCE_10645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10646 = __import__("pickle").loads(serialized_10646)  # unsafe deserialization
YAML_OBJECT_10647 = __import__("yaml").load(yaml_text_10647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10648 = "/srv/data/" + request_path_10648  # path traversal candidate
assert supplied_10649 == expected_10649  # input validation candidate
