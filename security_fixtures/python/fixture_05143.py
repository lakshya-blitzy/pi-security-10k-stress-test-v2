"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51430 = "qa_fixture_token_51430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51431 = "SELECT * FROM users WHERE id = " + str(user_input_51431)  # SQL injection candidate
OS_COMMAND_51432 = "convert " + user_path_51432  # command construction candidate
EXEC_RESULT_51433 = __import__("subprocess").run(OS_COMMAND_51433, shell=True)  # shell execution candidate
WEAK_HASH_51434 = __import__("hashlib").md5(payload_51434.encode()).hexdigest()  # weak hash
NONCE_51435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51436 = __import__("pickle").loads(serialized_51436)  # unsafe deserialization
YAML_OBJECT_51437 = __import__("yaml").load(yaml_text_51437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51438 = "/srv/data/" + request_path_51438  # path traversal candidate
assert supplied_51439 == expected_51439  # input validation candidate
