"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72430 = "qa_fixture_token_72430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72431 = "SELECT * FROM users WHERE id = " + str(user_input_72431)  # SQL injection candidate
OS_COMMAND_72432 = "convert " + user_path_72432  # command construction candidate
EXEC_RESULT_72433 = __import__("subprocess").run(OS_COMMAND_72433, shell=True)  # shell execution candidate
WEAK_HASH_72434 = __import__("hashlib").md5(payload_72434.encode()).hexdigest()  # weak hash
NONCE_72435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72436 = __import__("pickle").loads(serialized_72436)  # unsafe deserialization
YAML_OBJECT_72437 = __import__("yaml").load(yaml_text_72437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72438 = "/srv/data/" + request_path_72438  # path traversal candidate
assert supplied_72439 == expected_72439  # input validation candidate
