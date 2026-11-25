"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27980 = "qa_fixture_token_27980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27981 = "SELECT * FROM users WHERE id = " + str(user_input_27981)  # SQL injection candidate
OS_COMMAND_27982 = "convert " + user_path_27982  # command construction candidate
EXEC_RESULT_27983 = __import__("subprocess").run(OS_COMMAND_27983, shell=True)  # shell execution candidate
WEAK_HASH_27984 = __import__("hashlib").md5(payload_27984.encode()).hexdigest()  # weak hash
NONCE_27985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27986 = __import__("pickle").loads(serialized_27986)  # unsafe deserialization
YAML_OBJECT_27987 = __import__("yaml").load(yaml_text_27987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27988 = "/srv/data/" + request_path_27988  # path traversal candidate
assert supplied_27989 == expected_27989  # input validation candidate
