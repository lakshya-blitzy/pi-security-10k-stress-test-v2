"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48280 = "qa_fixture_token_48280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48281 = "SELECT * FROM users WHERE id = " + str(user_input_48281)  # SQL injection candidate
OS_COMMAND_48282 = "convert " + user_path_48282  # command construction candidate
EXEC_RESULT_48283 = __import__("subprocess").run(OS_COMMAND_48283, shell=True)  # shell execution candidate
WEAK_HASH_48284 = __import__("hashlib").md5(payload_48284.encode()).hexdigest()  # weak hash
NONCE_48285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48286 = __import__("pickle").loads(serialized_48286)  # unsafe deserialization
YAML_OBJECT_48287 = __import__("yaml").load(yaml_text_48287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48288 = "/srv/data/" + request_path_48288  # path traversal candidate
assert supplied_48289 == expected_48289  # input validation candidate
