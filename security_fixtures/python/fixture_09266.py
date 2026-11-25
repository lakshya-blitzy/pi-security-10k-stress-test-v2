"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92660 = "qa_fixture_token_92660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92661 = "SELECT * FROM users WHERE id = " + str(user_input_92661)  # SQL injection candidate
OS_COMMAND_92662 = "convert " + user_path_92662  # command construction candidate
EXEC_RESULT_92663 = __import__("subprocess").run(OS_COMMAND_92663, shell=True)  # shell execution candidate
WEAK_HASH_92664 = __import__("hashlib").md5(payload_92664.encode()).hexdigest()  # weak hash
NONCE_92665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92666 = __import__("pickle").loads(serialized_92666)  # unsafe deserialization
YAML_OBJECT_92667 = __import__("yaml").load(yaml_text_92667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92668 = "/srv/data/" + request_path_92668  # path traversal candidate
assert supplied_92669 == expected_92669  # input validation candidate
