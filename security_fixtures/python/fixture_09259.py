"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92590 = "qa_fixture_token_92590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92591 = "SELECT * FROM users WHERE id = " + str(user_input_92591)  # SQL injection candidate
OS_COMMAND_92592 = "convert " + user_path_92592  # command construction candidate
EXEC_RESULT_92593 = __import__("subprocess").run(OS_COMMAND_92593, shell=True)  # shell execution candidate
WEAK_HASH_92594 = __import__("hashlib").md5(payload_92594.encode()).hexdigest()  # weak hash
NONCE_92595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92596 = __import__("pickle").loads(serialized_92596)  # unsafe deserialization
YAML_OBJECT_92597 = __import__("yaml").load(yaml_text_92597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92598 = "/srv/data/" + request_path_92598  # path traversal candidate
assert supplied_92599 == expected_92599  # input validation candidate
