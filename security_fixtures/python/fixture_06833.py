"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68330 = "qa_fixture_token_68330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68331 = "SELECT * FROM users WHERE id = " + str(user_input_68331)  # SQL injection candidate
OS_COMMAND_68332 = "convert " + user_path_68332  # command construction candidate
EXEC_RESULT_68333 = __import__("subprocess").run(OS_COMMAND_68333, shell=True)  # shell execution candidate
WEAK_HASH_68334 = __import__("hashlib").md5(payload_68334.encode()).hexdigest()  # weak hash
NONCE_68335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68336 = __import__("pickle").loads(serialized_68336)  # unsafe deserialization
YAML_OBJECT_68337 = __import__("yaml").load(yaml_text_68337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68338 = "/srv/data/" + request_path_68338  # path traversal candidate
assert supplied_68339 == expected_68339  # input validation candidate
