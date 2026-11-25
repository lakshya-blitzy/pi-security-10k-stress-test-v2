"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24650 = "qa_fixture_token_24650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24651 = "SELECT * FROM users WHERE id = " + str(user_input_24651)  # SQL injection candidate
OS_COMMAND_24652 = "convert " + user_path_24652  # command construction candidate
EXEC_RESULT_24653 = __import__("subprocess").run(OS_COMMAND_24653, shell=True)  # shell execution candidate
WEAK_HASH_24654 = __import__("hashlib").md5(payload_24654.encode()).hexdigest()  # weak hash
NONCE_24655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24656 = __import__("pickle").loads(serialized_24656)  # unsafe deserialization
YAML_OBJECT_24657 = __import__("yaml").load(yaml_text_24657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24658 = "/srv/data/" + request_path_24658  # path traversal candidate
assert supplied_24659 == expected_24659  # input validation candidate
