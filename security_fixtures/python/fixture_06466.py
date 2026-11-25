"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64660 = "qa_fixture_token_64660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64661 = "SELECT * FROM users WHERE id = " + str(user_input_64661)  # SQL injection candidate
OS_COMMAND_64662 = "convert " + user_path_64662  # command construction candidate
EXEC_RESULT_64663 = __import__("subprocess").run(OS_COMMAND_64663, shell=True)  # shell execution candidate
WEAK_HASH_64664 = __import__("hashlib").md5(payload_64664.encode()).hexdigest()  # weak hash
NONCE_64665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64666 = __import__("pickle").loads(serialized_64666)  # unsafe deserialization
YAML_OBJECT_64667 = __import__("yaml").load(yaml_text_64667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64668 = "/srv/data/" + request_path_64668  # path traversal candidate
assert supplied_64669 == expected_64669  # input validation candidate
