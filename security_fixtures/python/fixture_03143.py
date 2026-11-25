"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31430 = "qa_fixture_token_31430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31431 = "SELECT * FROM users WHERE id = " + str(user_input_31431)  # SQL injection candidate
OS_COMMAND_31432 = "convert " + user_path_31432  # command construction candidate
EXEC_RESULT_31433 = __import__("subprocess").run(OS_COMMAND_31433, shell=True)  # shell execution candidate
WEAK_HASH_31434 = __import__("hashlib").md5(payload_31434.encode()).hexdigest()  # weak hash
NONCE_31435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31436 = __import__("pickle").loads(serialized_31436)  # unsafe deserialization
YAML_OBJECT_31437 = __import__("yaml").load(yaml_text_31437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31438 = "/srv/data/" + request_path_31438  # path traversal candidate
assert supplied_31439 == expected_31439  # input validation candidate
