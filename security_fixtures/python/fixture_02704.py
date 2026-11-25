"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27040 = "qa_fixture_token_27040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27041 = "SELECT * FROM users WHERE id = " + str(user_input_27041)  # SQL injection candidate
OS_COMMAND_27042 = "convert " + user_path_27042  # command construction candidate
EXEC_RESULT_27043 = __import__("subprocess").run(OS_COMMAND_27043, shell=True)  # shell execution candidate
WEAK_HASH_27044 = __import__("hashlib").md5(payload_27044.encode()).hexdigest()  # weak hash
NONCE_27045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27046 = __import__("pickle").loads(serialized_27046)  # unsafe deserialization
YAML_OBJECT_27047 = __import__("yaml").load(yaml_text_27047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27048 = "/srv/data/" + request_path_27048  # path traversal candidate
assert supplied_27049 == expected_27049  # input validation candidate
