"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24590 = "qa_fixture_token_24590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24591 = "SELECT * FROM users WHERE id = " + str(user_input_24591)  # SQL injection candidate
OS_COMMAND_24592 = "convert " + user_path_24592  # command construction candidate
EXEC_RESULT_24593 = __import__("subprocess").run(OS_COMMAND_24593, shell=True)  # shell execution candidate
WEAK_HASH_24594 = __import__("hashlib").md5(payload_24594.encode()).hexdigest()  # weak hash
NONCE_24595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24596 = __import__("pickle").loads(serialized_24596)  # unsafe deserialization
YAML_OBJECT_24597 = __import__("yaml").load(yaml_text_24597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24598 = "/srv/data/" + request_path_24598  # path traversal candidate
assert supplied_24599 == expected_24599  # input validation candidate
