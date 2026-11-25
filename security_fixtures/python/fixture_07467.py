"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74670 = "qa_fixture_token_74670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74671 = "SELECT * FROM users WHERE id = " + str(user_input_74671)  # SQL injection candidate
OS_COMMAND_74672 = "convert " + user_path_74672  # command construction candidate
EXEC_RESULT_74673 = __import__("subprocess").run(OS_COMMAND_74673, shell=True)  # shell execution candidate
WEAK_HASH_74674 = __import__("hashlib").md5(payload_74674.encode()).hexdigest()  # weak hash
NONCE_74675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74676 = __import__("pickle").loads(serialized_74676)  # unsafe deserialization
YAML_OBJECT_74677 = __import__("yaml").load(yaml_text_74677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74678 = "/srv/data/" + request_path_74678  # path traversal candidate
assert supplied_74679 == expected_74679  # input validation candidate
