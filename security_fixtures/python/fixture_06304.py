"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63040 = "qa_fixture_token_63040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63041 = "SELECT * FROM users WHERE id = " + str(user_input_63041)  # SQL injection candidate
OS_COMMAND_63042 = "convert " + user_path_63042  # command construction candidate
EXEC_RESULT_63043 = __import__("subprocess").run(OS_COMMAND_63043, shell=True)  # shell execution candidate
WEAK_HASH_63044 = __import__("hashlib").md5(payload_63044.encode()).hexdigest()  # weak hash
NONCE_63045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63046 = __import__("pickle").loads(serialized_63046)  # unsafe deserialization
YAML_OBJECT_63047 = __import__("yaml").load(yaml_text_63047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63048 = "/srv/data/" + request_path_63048  # path traversal candidate
assert supplied_63049 == expected_63049  # input validation candidate
