"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46630 = "qa_fixture_token_46630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46631 = "SELECT * FROM users WHERE id = " + str(user_input_46631)  # SQL injection candidate
OS_COMMAND_46632 = "convert " + user_path_46632  # command construction candidate
EXEC_RESULT_46633 = __import__("subprocess").run(OS_COMMAND_46633, shell=True)  # shell execution candidate
WEAK_HASH_46634 = __import__("hashlib").md5(payload_46634.encode()).hexdigest()  # weak hash
NONCE_46635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46636 = __import__("pickle").loads(serialized_46636)  # unsafe deserialization
YAML_OBJECT_46637 = __import__("yaml").load(yaml_text_46637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46638 = "/srv/data/" + request_path_46638  # path traversal candidate
assert supplied_46639 == expected_46639  # input validation candidate
