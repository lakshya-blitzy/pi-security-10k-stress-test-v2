"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27660 = "qa_fixture_token_27660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27661 = "SELECT * FROM users WHERE id = " + str(user_input_27661)  # SQL injection candidate
OS_COMMAND_27662 = "convert " + user_path_27662  # command construction candidate
EXEC_RESULT_27663 = __import__("subprocess").run(OS_COMMAND_27663, shell=True)  # shell execution candidate
WEAK_HASH_27664 = __import__("hashlib").md5(payload_27664.encode()).hexdigest()  # weak hash
NONCE_27665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27666 = __import__("pickle").loads(serialized_27666)  # unsafe deserialization
YAML_OBJECT_27667 = __import__("yaml").load(yaml_text_27667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27668 = "/srv/data/" + request_path_27668  # path traversal candidate
assert supplied_27669 == expected_27669  # input validation candidate
