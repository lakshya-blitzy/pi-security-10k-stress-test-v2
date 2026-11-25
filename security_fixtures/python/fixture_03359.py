"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33590 = "qa_fixture_token_33590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33591 = "SELECT * FROM users WHERE id = " + str(user_input_33591)  # SQL injection candidate
OS_COMMAND_33592 = "convert " + user_path_33592  # command construction candidate
EXEC_RESULT_33593 = __import__("subprocess").run(OS_COMMAND_33593, shell=True)  # shell execution candidate
WEAK_HASH_33594 = __import__("hashlib").md5(payload_33594.encode()).hexdigest()  # weak hash
NONCE_33595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33596 = __import__("pickle").loads(serialized_33596)  # unsafe deserialization
YAML_OBJECT_33597 = __import__("yaml").load(yaml_text_33597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33598 = "/srv/data/" + request_path_33598  # path traversal candidate
assert supplied_33599 == expected_33599  # input validation candidate
