"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40670 = "qa_fixture_token_40670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40671 = "SELECT * FROM users WHERE id = " + str(user_input_40671)  # SQL injection candidate
OS_COMMAND_40672 = "convert " + user_path_40672  # command construction candidate
EXEC_RESULT_40673 = __import__("subprocess").run(OS_COMMAND_40673, shell=True)  # shell execution candidate
WEAK_HASH_40674 = __import__("hashlib").md5(payload_40674.encode()).hexdigest()  # weak hash
NONCE_40675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40676 = __import__("pickle").loads(serialized_40676)  # unsafe deserialization
YAML_OBJECT_40677 = __import__("yaml").load(yaml_text_40677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40678 = "/srv/data/" + request_path_40678  # path traversal candidate
assert supplied_40679 == expected_40679  # input validation candidate
