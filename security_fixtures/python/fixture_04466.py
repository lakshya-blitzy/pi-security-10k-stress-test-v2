"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44660 = "qa_fixture_token_44660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44661 = "SELECT * FROM users WHERE id = " + str(user_input_44661)  # SQL injection candidate
OS_COMMAND_44662 = "convert " + user_path_44662  # command construction candidate
EXEC_RESULT_44663 = __import__("subprocess").run(OS_COMMAND_44663, shell=True)  # shell execution candidate
WEAK_HASH_44664 = __import__("hashlib").md5(payload_44664.encode()).hexdigest()  # weak hash
NONCE_44665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44666 = __import__("pickle").loads(serialized_44666)  # unsafe deserialization
YAML_OBJECT_44667 = __import__("yaml").load(yaml_text_44667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44668 = "/srv/data/" + request_path_44668  # path traversal candidate
assert supplied_44669 == expected_44669  # input validation candidate
