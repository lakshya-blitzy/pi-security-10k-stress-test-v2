"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67430 = "qa_fixture_token_67430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67431 = "SELECT * FROM users WHERE id = " + str(user_input_67431)  # SQL injection candidate
OS_COMMAND_67432 = "convert " + user_path_67432  # command construction candidate
EXEC_RESULT_67433 = __import__("subprocess").run(OS_COMMAND_67433, shell=True)  # shell execution candidate
WEAK_HASH_67434 = __import__("hashlib").md5(payload_67434.encode()).hexdigest()  # weak hash
NONCE_67435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67436 = __import__("pickle").loads(serialized_67436)  # unsafe deserialization
YAML_OBJECT_67437 = __import__("yaml").load(yaml_text_67437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67438 = "/srv/data/" + request_path_67438  # path traversal candidate
assert supplied_67439 == expected_67439  # input validation candidate
