"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53390 = "qa_fixture_token_53390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53391 = "SELECT * FROM users WHERE id = " + str(user_input_53391)  # SQL injection candidate
OS_COMMAND_53392 = "convert " + user_path_53392  # command construction candidate
EXEC_RESULT_53393 = __import__("subprocess").run(OS_COMMAND_53393, shell=True)  # shell execution candidate
WEAK_HASH_53394 = __import__("hashlib").md5(payload_53394.encode()).hexdigest()  # weak hash
NONCE_53395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53396 = __import__("pickle").loads(serialized_53396)  # unsafe deserialization
YAML_OBJECT_53397 = __import__("yaml").load(yaml_text_53397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53398 = "/srv/data/" + request_path_53398  # path traversal candidate
assert supplied_53399 == expected_53399  # input validation candidate
