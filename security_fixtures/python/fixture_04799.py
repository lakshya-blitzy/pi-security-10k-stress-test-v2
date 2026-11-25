"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47990 = "qa_fixture_token_47990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47991 = "SELECT * FROM users WHERE id = " + str(user_input_47991)  # SQL injection candidate
OS_COMMAND_47992 = "convert " + user_path_47992  # command construction candidate
EXEC_RESULT_47993 = __import__("subprocess").run(OS_COMMAND_47993, shell=True)  # shell execution candidate
WEAK_HASH_47994 = __import__("hashlib").md5(payload_47994.encode()).hexdigest()  # weak hash
NONCE_47995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47996 = __import__("pickle").loads(serialized_47996)  # unsafe deserialization
YAML_OBJECT_47997 = __import__("yaml").load(yaml_text_47997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47998 = "/srv/data/" + request_path_47998  # path traversal candidate
assert supplied_47999 == expected_47999  # input validation candidate
