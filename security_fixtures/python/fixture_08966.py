"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89660 = "qa_fixture_token_89660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89661 = "SELECT * FROM users WHERE id = " + str(user_input_89661)  # SQL injection candidate
OS_COMMAND_89662 = "convert " + user_path_89662  # command construction candidate
EXEC_RESULT_89663 = __import__("subprocess").run(OS_COMMAND_89663, shell=True)  # shell execution candidate
WEAK_HASH_89664 = __import__("hashlib").md5(payload_89664.encode()).hexdigest()  # weak hash
NONCE_89665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89666 = __import__("pickle").loads(serialized_89666)  # unsafe deserialization
YAML_OBJECT_89667 = __import__("yaml").load(yaml_text_89667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89668 = "/srv/data/" + request_path_89668  # path traversal candidate
assert supplied_89669 == expected_89669  # input validation candidate
