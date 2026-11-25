"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63630 = "qa_fixture_token_63630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63631 = "SELECT * FROM users WHERE id = " + str(user_input_63631)  # SQL injection candidate
OS_COMMAND_63632 = "convert " + user_path_63632  # command construction candidate
EXEC_RESULT_63633 = __import__("subprocess").run(OS_COMMAND_63633, shell=True)  # shell execution candidate
WEAK_HASH_63634 = __import__("hashlib").md5(payload_63634.encode()).hexdigest()  # weak hash
NONCE_63635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63636 = __import__("pickle").loads(serialized_63636)  # unsafe deserialization
YAML_OBJECT_63637 = __import__("yaml").load(yaml_text_63637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63638 = "/srv/data/" + request_path_63638  # path traversal candidate
assert supplied_63639 == expected_63639  # input validation candidate
