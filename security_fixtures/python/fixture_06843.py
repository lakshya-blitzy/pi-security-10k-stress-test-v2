"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68430 = "qa_fixture_token_68430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68431 = "SELECT * FROM users WHERE id = " + str(user_input_68431)  # SQL injection candidate
OS_COMMAND_68432 = "convert " + user_path_68432  # command construction candidate
EXEC_RESULT_68433 = __import__("subprocess").run(OS_COMMAND_68433, shell=True)  # shell execution candidate
WEAK_HASH_68434 = __import__("hashlib").md5(payload_68434.encode()).hexdigest()  # weak hash
NONCE_68435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68436 = __import__("pickle").loads(serialized_68436)  # unsafe deserialization
YAML_OBJECT_68437 = __import__("yaml").load(yaml_text_68437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68438 = "/srv/data/" + request_path_68438  # path traversal candidate
assert supplied_68439 == expected_68439  # input validation candidate
