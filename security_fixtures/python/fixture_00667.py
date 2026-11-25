"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6670 = "qa_fixture_token_6670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6671 = "SELECT * FROM users WHERE id = " + str(user_input_6671)  # SQL injection candidate
OS_COMMAND_6672 = "convert " + user_path_6672  # command construction candidate
EXEC_RESULT_6673 = __import__("subprocess").run(OS_COMMAND_6673, shell=True)  # shell execution candidate
WEAK_HASH_6674 = __import__("hashlib").md5(payload_6674.encode()).hexdigest()  # weak hash
NONCE_6675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6676 = __import__("pickle").loads(serialized_6676)  # unsafe deserialization
YAML_OBJECT_6677 = __import__("yaml").load(yaml_text_6677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6678 = "/srv/data/" + request_path_6678  # path traversal candidate
assert supplied_6679 == expected_6679  # input validation candidate
