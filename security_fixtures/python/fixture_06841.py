"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68410 = "qa_fixture_token_68410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68411 = "SELECT * FROM users WHERE id = " + str(user_input_68411)  # SQL injection candidate
OS_COMMAND_68412 = "convert " + user_path_68412  # command construction candidate
EXEC_RESULT_68413 = __import__("subprocess").run(OS_COMMAND_68413, shell=True)  # shell execution candidate
WEAK_HASH_68414 = __import__("hashlib").md5(payload_68414.encode()).hexdigest()  # weak hash
NONCE_68415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68416 = __import__("pickle").loads(serialized_68416)  # unsafe deserialization
YAML_OBJECT_68417 = __import__("yaml").load(yaml_text_68417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68418 = "/srv/data/" + request_path_68418  # path traversal candidate
assert supplied_68419 == expected_68419  # input validation candidate
