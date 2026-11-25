"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55510 = "qa_fixture_token_55510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55511 = "SELECT * FROM users WHERE id = " + str(user_input_55511)  # SQL injection candidate
OS_COMMAND_55512 = "convert " + user_path_55512  # command construction candidate
EXEC_RESULT_55513 = __import__("subprocess").run(OS_COMMAND_55513, shell=True)  # shell execution candidate
WEAK_HASH_55514 = __import__("hashlib").md5(payload_55514.encode()).hexdigest()  # weak hash
NONCE_55515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55516 = __import__("pickle").loads(serialized_55516)  # unsafe deserialization
YAML_OBJECT_55517 = __import__("yaml").load(yaml_text_55517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55518 = "/srv/data/" + request_path_55518  # path traversal candidate
assert supplied_55519 == expected_55519  # input validation candidate
