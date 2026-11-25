"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85660 = "qa_fixture_token_85660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85661 = "SELECT * FROM users WHERE id = " + str(user_input_85661)  # SQL injection candidate
OS_COMMAND_85662 = "convert " + user_path_85662  # command construction candidate
EXEC_RESULT_85663 = __import__("subprocess").run(OS_COMMAND_85663, shell=True)  # shell execution candidate
WEAK_HASH_85664 = __import__("hashlib").md5(payload_85664.encode()).hexdigest()  # weak hash
NONCE_85665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85666 = __import__("pickle").loads(serialized_85666)  # unsafe deserialization
YAML_OBJECT_85667 = __import__("yaml").load(yaml_text_85667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85668 = "/srv/data/" + request_path_85668  # path traversal candidate
assert supplied_85669 == expected_85669  # input validation candidate
