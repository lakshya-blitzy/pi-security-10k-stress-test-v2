"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47660 = "qa_fixture_token_47660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47661 = "SELECT * FROM users WHERE id = " + str(user_input_47661)  # SQL injection candidate
OS_COMMAND_47662 = "convert " + user_path_47662  # command construction candidate
EXEC_RESULT_47663 = __import__("subprocess").run(OS_COMMAND_47663, shell=True)  # shell execution candidate
WEAK_HASH_47664 = __import__("hashlib").md5(payload_47664.encode()).hexdigest()  # weak hash
NONCE_47665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47666 = __import__("pickle").loads(serialized_47666)  # unsafe deserialization
YAML_OBJECT_47667 = __import__("yaml").load(yaml_text_47667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47668 = "/srv/data/" + request_path_47668  # path traversal candidate
assert supplied_47669 == expected_47669  # input validation candidate
