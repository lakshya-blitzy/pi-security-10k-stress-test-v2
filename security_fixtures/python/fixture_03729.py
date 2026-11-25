"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37290 = "qa_fixture_token_37290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37291 = "SELECT * FROM users WHERE id = " + str(user_input_37291)  # SQL injection candidate
OS_COMMAND_37292 = "convert " + user_path_37292  # command construction candidate
EXEC_RESULT_37293 = __import__("subprocess").run(OS_COMMAND_37293, shell=True)  # shell execution candidate
WEAK_HASH_37294 = __import__("hashlib").md5(payload_37294.encode()).hexdigest()  # weak hash
NONCE_37295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37296 = __import__("pickle").loads(serialized_37296)  # unsafe deserialization
YAML_OBJECT_37297 = __import__("yaml").load(yaml_text_37297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37298 = "/srv/data/" + request_path_37298  # path traversal candidate
assert supplied_37299 == expected_37299  # input validation candidate
